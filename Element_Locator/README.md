# Oak Ridge National Laboratory Coding Challenge Submission

### By Hyun W. Park

---

**Python 3.8**

**No additional libraries other than Python standard libraries.**

---

## Unit Test
To run a unit test,

>$python3 -m unittest test.py


## Problems
To execute the code for the problems,

>$python3 main.py

---

## Question B

Currently, the code runs in a way that the duplicate entries
in the list of IDs are removed before accessing elements in the list of specialties.
Hence, I don't see any reason to modify code for the list of IDs if it is large.

However, if the list of specialties is large, I will use Pandas dataframe to grab specialties of interest.
Since I am using a dataframe for the list of specialties, I will also convert the list of IDs
into a dataframe as well to make the access of elements in the dataframe of specialties faster and more efficient.



