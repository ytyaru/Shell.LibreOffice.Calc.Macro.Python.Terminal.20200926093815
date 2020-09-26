#!/usr/bin/env bash
set -Ceu
#---------------------------------------------------------------------------
# LibreOffice-CalcのPythonマクロを端末で実行する。
# CreatedAt: 2020-09-26
#---------------------------------------------------------------------------
Run() {
	THIS="$(realpath "${BASH_SOURCE:-0}")"; HERE="$(dirname "$THIS")"; PARENT="$(dirname "$HERE")"; THIS_NAME="$(basename "$THIS")"; APP_ROOT="$PARENT";
	cd "$HERE"
	soffice --calc --headless "--accept=pipe,name=librepipe;urp;"
}
Run "$@"
