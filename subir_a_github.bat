@echo off
title Subiendo proyecto a GitHub - Juan Esteban Ospina Zapata
color 0B
echo ======================================================================
echo    SUBIENDO TU PROYECTO ACTUALIZADO A GITHUB (Juan112021)
echo ======================================================================
echo.
cd /d "c:\INGENIERIA INFORMATICA\SEXTO SEMESTRE\parcial_juanes"

echo [1/2] Subiendo rama feature/quiz-interactivo...
git push -u origin feature/quiz-interactivo
echo.

echo [2/2] Subiendo rama main...
git push origin main
echo.

echo ======================================================================
echo    SUBIDA FINALIZADA CON EXITO. REVISA TU GITHUB.
echo ======================================================================
echo.
pause
