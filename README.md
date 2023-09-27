# JavaScript Data Race Tracer

## Overview

This repository uses [Jalangi2](https://github.com/Samsung/jalangi2), created by Samsung Electronics Ltd., 
to create reproducible data traces in the .std format.

Code may be converted to ES5-compatible code through [babel](https://babeljs.io/).

## Setup

- Install [node.js](https://nodejs.org/en), which includes the npm package manager.
- Clone the tracer repository.
- Navigate into the jalangi2 directory.
- Run `npm install` in the jalangi2 directory to install both jalangi2 and babel using npm.
### Running browser traces
If traces are to be run from within a browser, two approaches are available. Both approaches require a valid localhost SSL certificate.
In order to generate locally trusted SSL certificates, [mkcert](https://github.com/FiloSottile/mkcert) is a good option.
Please ensure that the certificate is trusted by the environment, instead of granting a security exception, as these may interfere with some functionality.

For manual instrumentation, install the npm package [httpserver](https://www.npmjs.com/package/http-server).
It is necessary to host the files over an SSL/HTTPS connection, as the logger requires access to the OPFS.
Navigate to the directory containing your instrumented files, and run http-server using the generated certificates:
```bash
sudo http-server -S -C $SSL_CERT_DIR/cert.pem -K $SSL_CERT_DIR/key.pem
```

For automated instrumentation, [install mitmproxy](https://mitmproxy.org/), with exact instructions depending on your environment.
For the existing mitmproxy scripts, standalone mitmproxy binaries, version 9.0.1, were used. The binaries were placed 
in a subdirectory called "mitmproxy9.0.1". You will need the `mitmdump` binary 
and a locally trusted certificate for HTTPS support. To set up https for Mitmproxy, please [follow the official documentation](https://docs.mitmproxy.org/stable/concepts-certificates/).
Once correctly set up, you may use `scripts/runMitmproxy.sh` to start the proxy, and use `scripts/runProxyChromium.sh` to create a Chromium web browser that has been configured to use the proxy.

Note that without additional modification, the mitmproxy approach will not be able to instrument files that have been written in newer standards than ES5.
This is a technical limitation of Jalangi2. It may be possible to create an additional plugin for `mitmdump` that pipes all content through babel before instrumentation.


## Usage

Please note that due to technical limitations, it may be necessary to convert code you wish to create a trace of into ES5-compatible code.
babel may be used for these efforts.

The tracer analysis is located in `jalangi2/src/js/sample_analyses/trace/EventActionTraceLogger.js.`
Execution depends on the Jalangi2 SMemory module, and the ChainedAnalyses module.

### Node.js: Instrumentation and tracing

To create a trace file, run the jalangi.js command with ChainedAnalyses.js, SMemory.js, and EventActionTracerLogger.js.
The trace will be generated as `trace.log` in the jalangi2 directory.

```bash
# This snippet may be executed by executing npm run runTraceDeltablue
node src/js/commands/jalangi.js --inlineIID --inlineSource --analysis src/js/sample_analyses/ChainedAnalyses.js --analysis src/js/runtime/SMemory.js --analysis src/js/sample_analyses/trace/EventActionTraceLogger.js tests/octane/deltablue.js
```
### Browser: Manual instrumentation

If the code to be tested uses ES6 or newer, it is necessary to transpile the code using babel before instrumenting it with jalangi2.
Please use `babel -d $OUTPUT_DIRECTORY $FILES_TO_TRANSPILE` to convert any code into ES5-compatible code.

To instrument the code and prepare it for execution in a browser, use the `instrument.js` command provided by Jalangi2.
The same instrumentation scripts as with direct execution in node.js are necessary. Supply an `--outputDir` to the command,
otherwise instrument.js will fail to execute.

```bash
node src/js/commands/instrument.js --inlineIID --inlineSource --inlineJalangi --analysis src/js/sample_analyses/ChainedAnalyses.js --analysis src/js/runtime/SMemory.js --analysis src/js/sample_analyses/trace/EventActionTraceLogger.js --outputDir ../basicTests/jalangi_out/intervalTest ../basicTests/babelified/intervalTest
```


A fully chained manual instrumentation can be found by executing `npm run instrumentIntervalTest`.


### Browser: Instrumented code execution
In order for the trace to be properly stored, it is necessary to 
Open the previously instrumented files in a webbrowser. Samsung recommends using Chrome or its derivatives.
Firefox has proven itself to work in local tests.

To finalize the trace, use the keybind `Alt+Shift+T`. The generated trace should open in a new tab.
If it does not, or the code refuses to run, please check the browser console for errors.
The most common causes for errors are either attempts to instrument non-ES5 code, or an invalid HTTPS setup.



