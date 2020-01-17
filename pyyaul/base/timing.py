#! /usr/bin/env python3.7

import time



def timestamp(t=None):
	"""
	@param t `float` seconds since epoch as returned by `time.time`.  If `None`, will use the
		current time.
	@return `str` timestamp of the format "YYYY.mm.dd.HH.MM.SS".
	"""
	if t is None:
		t = time.time()
	return time.strftime('%Y.%m.%d.%H.%M.%S')
