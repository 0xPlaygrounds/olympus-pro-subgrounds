# Subgrounds + Olympus Pro subgraph
A miniature Python library which includes functions to fetch all the entities of a certain type and return their data in a pandas DataFrame. All the library code can be found in the `data_fetcher` module. The repo comes with a notebook file `demo.ipynb` which showcases the library functions in action.

The library relies almost entirely on the Subgrounds library, which can be found [here](https://github.com/Protean-Labs/subgrounds).

The subgraph used in this library can be found [here](https://github.com/0xPlaygrounds/olympus-pro-subgraph).

## Installation
To install this library and run the notebook, pipenv must first be installed using the following command:<br>`pip install pipenv`

Then, from the root of the project repository, run:<br>`pipenv install`

### Notebook setup
Execute the following commands:
- Log onto the pipenv virtual environment: `pipenv shell`
- Create the Jupyter kernel: `python -m ipykernel install --user --name=olympus-pro-subgrounds`
- Start the notebook server: `jupyter notebook`

Then, open and run the `demo.ipynb` notebook. IMPORTANT: Remember to set the active kernel to `olympus-pro-subgrounds` (`Kernel` > `Change kernel`).

## Integration
To integrate this miniature library in an existing project, you must first upgrade your Python version to **3.10 or higher** (required by `subgrounds`). This will vary depending on your Python package manager and operating system. 

Then install `subgrounds` using your Python package manager.

Once the dependencies are installed, you can copy the `data_fetcher.py` module into your project repository to start using the library.
