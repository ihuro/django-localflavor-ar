=====================
django_localflavor_ar
=====================

Country-specific Django helpers for Argentina.

What's in the Argentina localflavor?
====================================

.. class:: ar.forms.ARPostalCodeField

    A form field that validates input as either a classic four-digit Argentinian
    postal code or a CPA_.

.. _CPA: http://www.correoargentino.com.ar/consulta_cpa/home.php

.. class:: ar.forms.ARDNIField

    A form field that validates input as a Documento Nacional de Identidad (DNI)
    number.

.. class:: ar.forms.ARCUITField

    A form field that validates input as a Codigo Unico de Identificacion
    Tributaria (CUIT) number.

.. class:: ar.forms.ARProvinceSelect

    A ``Select`` widget that uses a list of Argentina's provinces and autonomous
    cities as its choices.

See the source code for full details.

About localflavors
==================

Django's "localflavor" packages offer additional functionality for particular
countries or cultures.

For example, these might include form fields for your country's postal codes,
phone number formats or government ID numbers.

This code used to live in Django proper -- in django.contrib.localflavor -- but
was separated into standalone packages in Django 1.5 to keep the framework's
core clean.

For a full list of available localflavors, see https://github.com/django/
