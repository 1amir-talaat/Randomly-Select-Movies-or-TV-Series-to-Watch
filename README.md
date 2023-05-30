# Randomly Select and Watch Movies or TV Series

This Python code help to select and watch a movie or TV series from a specified directory of movies or series. 

## How it Works

You prompted to choose between watching a movie or TV series. Based on their input, the code retrieves a list of movies or series from the specified directory using the `os` library. It then selects a random movie or series that has not been watched before, based on a list of watched movies or series stored in a `watched.txt` file. 

The selected movie or series is printed to the console using colored text output from the `rich` library. The user is then prompted to confirm whether they want to watch it or not. If they confirm, the code stores the selected movie or series in the `watched.txt` file and exits. If they decline, the code prompts the user to select another movie or series.

## Requirements

- Python 3.x
- `rich` library (install using `pip install rich`)

## How to Use

1. Cloneor download the repository to your computer.
2. Open a terminal or command prompt and navigate to the directory containing the code.
3. Run the script using `python random_movie.py`.
4. Follow the prompts to select and watch a movie or TV series.

## License

This code is licensed under the [MIT License](https://github.com/yourusername/random-movie/blob/main/LICENSE). Feel free to use it however you like!

## Acknowledgements

This code was written by [Amir Talaat](https://github.com/1amir-talaat). Special thanks to the following libraries used in this project:

- [os](https://docs.python.org/3/library/os.html) - for accessing the file system
- [random](https://docs.python.org/3/library/random.html) - for selecting a random movie or series
- [rich](https://rich.readthedocs.io/en/stable/) - for colored text output on the console.
