﻿
// специальный скрипт для обхода проблемы с ЭтотОбъект https://bitbucket.org/EvilBeaver/1script/issue/58/------------------------------------------

ТекПуть = Новый Файл(ТекущийСценарий().Источник).Путь;
ПодключитьСценарий(ТекПуть + "\testrunner.os", "ЗапускательТестов");

ЗапускательТестов = Новый ЗапускательТестов();
ЗапускательТестов.ВыполнитьТесты(АргументыКоманднойСтроки);

ЗавершитьРаботу(ЗапускательТестов.ПолучитьРезультатТестирования());
