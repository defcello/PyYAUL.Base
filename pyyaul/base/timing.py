#! /usr/bin/env python3.7

from enum import Enum
from calendar import timegm
import time





TIMESTAMPFORMATS = Enum('TIMESTAMPFORMATS',
	(
		'DATETIMESEC_DOTS',
		'MMDDYYYY_SLASHES',
	),
)

def timestamp(t=None, f=TIMESTAMPFORMATS.DATETIMESEC_DOTS):
	"""
	@param t `float` seconds since epoch as returned by `time.time`.  If `None`, will use the
		current time.
	@return `str` timestamp of the format "YYYY.mm.dd.HH.MM.SS".
	"""
	if t is None:
		t = time.time()
	if f is TIMESTAMPFORMATS.DATETIMESEC_DOTS:
		tStr = time.strftime('%Y.%m.%d.%H.%M.%S')
	elif f is TIMESTAMPFORMATS.MMDDYYYY_SLASHES:
		tStr = time.strftime('%m/%d/%Y')
	else:
		raise ValueError(f'Unexpected format: f={f!r}')
	return tStr

def timestampParse(tStr, f=TIMESTAMPFORMATS.DATETIMESEC_DOTS):
	"""
	@param t `float` seconds since epoch as returned by `time.time`.  If `None`, will use the
		current time.
	@return `str` timestamp of the format "YYYY.mm.dd.HH.MM.SS".
	"""
	if f is TIMESTAMPFORMATS.DATETIMESEC_DOTS:
		t = timegm(time.strptime(tStr, '%Y.%m.%d.%H.%M.%S'))
	elif f is TIMESTAMPFORMATS.MMDDYYYY_SLASHES:
		t = timegm(time.strptime(tStr, '%m/%d/%Y'))
	else:
		raise ValueError(f'Unexpected format: f={f!r}')
	return t
