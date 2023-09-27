if [ -z "$1" ]
then
  echo "No test to transpile specified"
  exit 1;
fi
SRC_DIR=$(readlink -m "$1")
TARGET_DIR=$(basename "$SRC_DIR")
BABEL_DIR=$(builtin cd "$SRC_DIR/.." || exit 2; pwd)"/babelified/"$TARGET_DIR
echo "Copying any found non-js/non-ts files from $SRC_DIR to $BABEL_DIR..."
find "$SRC_DIR" -type f ! \( -iname "*.js" -o -iname "*.ts" \) -exec cp {} "$BABEL_DIR" \;
