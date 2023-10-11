
-- project needs python 3
-- unzip project.zip -d /path/to/extract/to
-- cd /path/to/extract/to/project-directory 
-- python3 -m venv myenv 
# On Unix or MacOS:
-- source myenv/bin/activate
# On Windows:
-- myenv\Scripts\activate
-- pip install -r requirements.txt
-- run  python3 src/lookup.py to lookup price of symbol on a date
-- run  python3 src/lowest_highest.py to check lowest and highest price for given date range

-- Q & A
- What compromises did you make due to time constraints? - I implemented all features
- How would you approach versioning of this library? - I can have another api in library which tells version, or can have version file
- How would we go about publishing this library? - I can publish this on GITHUB under MIT licence
- How would you design this if it was going to be a service rather than a library? - We can use something like AWS Lamda to host this as service
- Please include any other comments about your implementation. - Nothing I can think for now
- How much time did you spend on this exercise? - 2 hours
- Please include any general feedback you have about the exercise. - It was good learning and fun coding for me.
