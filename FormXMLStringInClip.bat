::<License>------------------------------------------------------------
::
:: Copyright (c) 2023 Shinnosuke Yakenohara
::
:: This program is free software: you can redistribute it and/or modify
:: it under the terms of the GNU General Public License as published by
:: the Free Software Foundation, either version 3 of the License, or
:: (at your option) any later version.
::
:: This program is distributed in the hope that it will be useful,
:: but WITHOUT ANY WARRANTY; without even the implied warranty of
:: MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
:: GNU General Public License for more details.
::
:: You should have received a copy of the GNU General Public License
:: along with this program.  If not, see <http://www.gnu.org/licenses/>.
::
::-----------------------------------------------------------</License>

:: <CAUTION!>
:: このファイルは文字コード `SJIS` で保存すること
:: </CAUTION!>

::
:: このバッチファイルが配置されたディレクトリに対して `dir` コマンドを実行し、  
:: 結果をテキストファイルに保存、そのファイルを開く  

@ echo off

set pyFileName=form.py
set pyFileFullPath=%~dp0%pyFileName%

py "%pyFileFullPath%"

:: Exception 発生時 ("syntax error" を想定) の場合 pause
if %errorlevel% neq 0 pause
