from typing import Callable, Any
import pandas as pd
import copy
import time
import MergeSort as ms
import QuickSort as qs
import BubbleSort as bs
import matplotlib.pyplot as plt

# Defining the column names
column_names = ['id', 'name', 'nationality', 'city',
                'latitude', 'longitude', 'gender', 'ethnic.group', 'age',
                'english.grade', 'math.grade', 'sciences.grade', 'language.grade', 'portfolio.rating',
                'coverletter.rating', 'refletter.rating']
Column_Selected = ['id', 'name', 'gender', 'math.grade']


# Defining data filtering function
def data_filtering(file_location):
    # Read the CSV file into a DataFrame
    df = pd.read_csv(file_location)
    return df


def sort_dataframe(df, key_func, algorithm='quicksort'):
    # Convert DataFrame to list of dictionaries
    data = df.to_dict('records')

    # Copying the original data to use in sorting algorithms
    data_copy = copy.deepcopy(data)

    # Apply the sorting algorithm
    if algorithm == 'quicksort':
        sorted_data = qs.quick_sort(data_copy, key_func)
    elif algorithm == 'merge_sort':
        sorted_data = ms.merge_sort(data_copy, key_func)
    elif algorithm == 'bubble_sort':
        sorted_data = bs.bubble_sort(data_copy, key_func)
    else:
        raise ValueError(f"Unknown sorting algorithm: {algorithm}")

    # Convert sorted list of dictionaries back to DataFrame
    sorted_df = pd.DataFrame(sorted_data, columns=Column_Selected)

    return sorted_df


def timeit(func, *args, **kwargs):
    start_time = time.time()
    result = func(*args, **kwargs)
    end_time = time.time()
    execution_time = (end_time - start_time) * 1000  # Convert to milliseconds
    return result, execution_time


# Main function
def main():
    # File location
    file_location = "student_db.csv"

    # Defining the key function for sorting by math.grade
    key_func_math_grade: Callable[[Any], Any] = lambda x: x['math.grade']

    # Filtering data
    pd.set_option('display.max_rows', None)
    df = data_filtering(file_location)
    selected_columns = df[Column_Selected]

    # Sorting DataFrame using multiple algorithms
    algorithms = ('quicksort', 'merge_sort', 'bubble_sort')
    execution_times = []
    for algorithm in algorithms:
        sorted_df, execution_time = timeit(sort_dataframe, selected_columns, key_func_math_grade, algorithm)
        print(f"Sorted DataFrame using {algorithm}:")
        print(sorted_df)
        print(f"Time taken (milliseconds) for {algorithm}: {execution_time}")
        execution_times.append(execution_time)

    plt.figure(figsize=(10, 6))
    plt.bar(algorithms, execution_times)
    plt.title('Execution Time of Sorting Algorithms')
    plt.xlabel('Algorithm')
    plt.ylabel('Execution Time (milliseconds)')
    plt.show()


if __name__ == "__main__":
    main()
