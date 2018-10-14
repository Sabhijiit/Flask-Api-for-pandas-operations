# Flask-Api for pandas operations

This project aims to perform certain `Pandas` operations on the given dataset and then serve the outputs of said operations through a flask API.

It has the following parts:
1. mass_spec_data.xlsx: the dataset
2. templates - folder containing the upload.html file where the file is uploaded
3. uploaded_file - folder that contains all the uploaded files, only .xlsx and .csv files are premitted.
4. pandasOperations.py - file with all the pandas logic
5. API.py - file that creates the flask server, performs uploading and from where all other api's are also called.

Steps to run the application:
1. run uploaded.py
2. go to localhost:5000/upload
3. click on submit query button to submit after selecting file. File name will be displayed to confirm upload. If file type is not permitted, page refreshes.
4. after uploading, the answer.py file is automatically executed to perform and all the pandas operations and the resulting dataframes are saved as .csv files in the "uploaded_file" directory.
5. then call any of the following api's to obtain the corresponding output:
	a. localhost:5000/q1/PC
	b. localhost:5000/q1/LPC
	c. localhost:5000/q1/plasmalogen
	d. localhost:5000/q2/data_new
	e. localhost:5000/q3/sample_means
