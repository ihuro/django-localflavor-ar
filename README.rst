=====================
django_localflavor_ar
=====================

Country-specific Django helpers for Argentina.

What's in the Argentina localflavor?
====================================

Forms
-----

* forms.ARPostalCodeField: A form field that validates input as either a
  classic four-digit Argentinian postal code or a CPA_.

* forms.ARDNIField: A form field that validates input as a Documento Nacional
  de Identidad (DNI) number.

* forms.ARCUITField: A form field that validates input as a Codigo Unico de
  Identificacion Tributaria (CUIT) number.

* forms.ARProvinceSelect: A ``Select`` widget that uses a list of Argentina's
  provinces and autonomous cities as its choices.

Models
------

* models.ARPostalCodeField: A model field that use forms.ARPostalCodeField as
  input widget.

* models.ARDNIField:  A model field that use forms.ARDNIField as input widget.

* models.ARCUITField:  A model field that use forms.ARCUITField as input widget.

* models.ARProvinceField:  A model field that use forms.ARProvinceField as
  input widget.

.. _CPA: http://www.correoargentino.com.ar/consulta_cpa/home.php

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
