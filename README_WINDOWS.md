# Windows Kurulum

1. ZIP dosyasini Windows'a indirin.
2. ZIP'i tamamen cikartin veya `KUR_WINDOWS.bat` dosyasini cikartilmis klasorden calistirin.
3. Gecici ZIP klasorunde `api`, `web` veya `ozcod` gorunmuyorsa BAT, Downloads/Desktop/Documents altinda `OZNUR_AI_FULL_PRO*.zip` arar.
4. Buldugu ZIP'i PowerShell `Expand-Archive` ile `%LOCALAPPDATA%\OZNUR_AI_FULL_PRO` altina cikarir.
5. Python sanal ortami olusturulur.
6. API syntax testi ve dahili unittest testleri yapilir.
7. Basariliysa PWA baslatilabilir.

Not: Kurulum BAT dosyasi UTF-8 BOM olmadan kaydedilmistir. CMD icinde `´╗┐@echo off` hatasi olusmamasi gerekir.
