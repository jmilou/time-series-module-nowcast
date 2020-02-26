## Time Series Module
This module is part of the [NOWCAST](https://github.com/tomasrojasc/NOWCAST) proyect by [ESO](https://www.eso.org) that aims to do short-term-forecast of the [seeing](https://en.wikipedia.org/wiki/Astronomical_seeing) parameter in order to improve astronomical observations. This module takes the cdv data and outputs a binary pandas dataframe file that can be used by the visualization app.


## How it works

### Setup
The first thing this module does is taking the two files in the folder ``files_to_process``. This files have to be named ``file1.csv`` and ``file2.csv`` and they have to have the structure specified in ``files_to_process/README.md``. Once those files are in place, it separates the time series in UT time intervals nights, for this it considers a day being from 22ºº hrs to 11ºº of the next day, and the label of the day is given by the first day.

If you want to change the UT time interval, it can be done in the ``modules/config.py`` file.

### Execution

Once That is done, you have to execute the ``main.py`` file.
