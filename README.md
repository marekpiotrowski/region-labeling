# Description
Package counts regions (or "islands") within a "binary" map of the following form:
```
110000000
111000100
110001110
000001100
001000000
110000000
000001100
```
Map shall consist solely of 1s and 0s and a newline in each row, without any whitespaces in-between.
It's assumed that `1` represents "land" and `0` represents "water".

# Running the application
Package's main is runnable as a "stand-alone" script (without any external dependencies, **besides python3**). 
For convenience, a shell script has been prepared. Script expects relative map file path to be provided via
command-line arguments:
```
$ ./count_islands.sh <map_file_path_relative_to_cwd>
```
For example (assuming we're in the repository root):
```
user:~/region-labeling$ ./count_islands.sh region_labeling/test/test_data/simple_map_pdf.txt
```
The script shall yield number of "regions" or "islands" within a given map.

python3 has been hardcoded as the interpreter.

Alternatively, if you want to run the application using interpreter of your desire, application can be run as follows:
```
user:~/region-labeling$ python3 -m region_labeling region_labeling/test/test_data/simple_map_pdf.txt
```

# Running tests
Considering tests rely on pytest, requirements will have to be installed. **It's strongly advised
to create a virtual environment at this point, as we wouldn't like to pollute system with necessary packages**.

Procedure for virtual environment creation and running tests:
```
user:~/region-labeling$ python3 -m venv venv
user:~/region-labeling$ source venv/bin/activate
user:~/region-labeling$ pip install -r requirements.txt
(venv) user:~/region-labeling$ pytest --pyargs region_labeling
```