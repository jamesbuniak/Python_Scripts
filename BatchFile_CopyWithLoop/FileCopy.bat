@echo off
set source=C:\PythonScripts\CreateMultipleFiles\Example\Example.L5X
set destination=C:\PythonScripts\CreateMultipleFiles\Example\CopyFolder\XVCW_%%A_XV.L5X

for /l %%A in (1,1,600) do copy %source% %destination%