@echo off
setlocal enabledelayedexpansion

:: Configuración del programa
set PROGRAM=ia_3_code_r_0.py
echo =================================================
echo  TESTING: %PROGRAM%
echo =================================================

:: Definición de Casos de Prueba (Entrada|Salida Esperada)
:: No dejes espacios alrededor del símbolo "|"
set "test1=10 5 8 20|5 8 10 20"
set "test2=1 2 3 4|1 2 3 4"
set "test3=9 1 7 2|1 2 7 9"
set "test4=100 0 -5 50|-5 0 50 100"
set "test5=20 19 18 17 16 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30|1 2 3 4 5 6 7 8 9 10 11 11 12 12 13 13 14 14 15 15 16 16 17 17 18 18 19 19 20 20 21 22 23 24 25 26 27 28 29 30"
:: Contador de éxitos
set /a passed=0

:: Ciclo para recorrer los 5 casos
for /l %%n in (1,1,5) do (
for /f "tokens=1,2 delims=|" %%a in ("!test%%n!") do (
set "IN=%%a"
set "EXPECTED=%%b"

    echo [Prueba %%n] Entrada: !IN!
    
    :: Ejecutar programa enviando entrada por STDIN
    echo !IN! | python %PROGRAM% > actual.txt
    
    :: Crear archivo con salida esperada (sin espacios extra)
    echo !EXPECTED!> expected.txt
    
    :: Comparar archivos
    fc actual.txt expected.txt >nul

    if !errorlevel! equ 0 (
        set /p GOT=<actual.txt
        echo [Prueba %%n]  Salida: !GOT!
        echo   [OK] Resultado correcto.
        set /a passed+=1
    ) else (
        echo   [ERROR] Fallo en la prueba %%n.
        echo   Esperado: [!EXPECTED!]
        set /p GOT=<actual.txt
        echo   Obtenido: [!GOT!]
    )
    echo -------------------------------------------------
)


)

echo.
echo Resumen: !passed! de 5 pruebas pasaron con exito.

:: Limpieza
if exist actual.txt del actual.txt
if exist expected.txt del expected.txt

pause