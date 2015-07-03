@echo off

rem C:\Python27\Scripts\scrapy.exe crawl lbc

set output=results.json
IF EXIST %output% del /F %output%
C:\Python27\Scripts\scrapy.exe crawl lbc -o %output%
