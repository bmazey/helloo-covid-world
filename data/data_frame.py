import pandas


def print_dataframe(file):
    df = pandas.read_csv(file)
    print(df)


if __name__ == '__main__':
    print_dataframe('data.csv')
