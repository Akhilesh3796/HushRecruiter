import itertools
import random
import pandas as pd
import ast


COUNT_OF_EMAILS = 5373
def generating_emails():
    email_list = []
    random_first_names = ["john", "jim", "roy", "michael", "james", "leroy", "curtis", "martin", "alex", "max_munster", "jack"]
    random_last_names = ["justin", "hoff", "webster", "schulz", "hefter", "mueller", "lahm", "ramsey", "ericson", "rose"]
    for idx in range(0, COUNT_OF_EMAILS):
        r_no = random.randint(0, COUNT_OF_EMAILS)
        r_first_email = random_first_names[random.randint(0, len(random_first_names)-1)]
        r_last_email = random_first_names[random.randint(0, len(random_last_names)-1)]
        email = r_first_email + r_last_email + str(r_no) + '@gmail.com'
        email_list.append(email)
    print("reached generating_emails")
    return email_list


def stackoverflow_data_reading():
    stack_1 = pd.read_csv(r"../data_files/stack_1.csv")
    stack_2 = pd.read_csv(r"../data_files/stack_2.csv")
    stack_3 = pd.read_csv(r"../data_files/stack_3.csv")
    stackoverflow_df = stack_1.append(stack_2).append(stack_3)

    print("reached stackoverflow_data_reading")
    return stackoverflow_df


def github_and_twitter_reading():
    github_data = pd.read_csv(r"../data_files/GitUserData.csv")
    tweet_data = pd.read_csv(r'../data_files/tweetData.csv')
    print("reached github_and_twitter_reading")
    return github_data, tweet_data


def preprocessing_data(tweet_data, stack_data):
    tweet_data = tweet_data.dropna()
    tweet_data['tweet'] = tweet_data['tweet'].apply(ast.literal_eval).str.decode("utf-8")
    tweet_data['tweet_username'] = tweet_data['tweet_username'].apply(ast.literal_eval).str.decode("utf-8")
    tweet_data['tweet_ip_address'] = tweet_data['tweet_ip_address'].apply(ast.literal_eval).str.decode("utf-8")
    tweet_data = tweet_data[tweet_data['tweet'].str.contains('Python | pyspark | sql | aws | docker')]
    print("reached preprocessing_data")
    return tweet_data, stack_data


def merging_data():
    email_list = generating_emails()
    stack_data = stackoverflow_data_reading()
    github_data, tweet_data = github_and_twitter_reading()
    tweet_data_final, stack_data_final = preprocessing_data(tweet_data, stack_data)

    stack_data_final = stack_data_final.sample(COUNT_OF_EMAILS).reset_index(drop=True)
    github_data = github_data.sample(COUNT_OF_EMAILS).reset_index(drop=True)
    tweet_data_final = tweet_data_final.sample(COUNT_OF_EMAILS).reset_index(drop=True)
    full_candidate_data = stack_data_final.join(github_data).join(tweet_data_final)

    full_candidate_data['email_id'] = email_list
    print("reached merging data")
    return full_candidate_data


merged_data = merging_data()
merged_data.to_csv('../data_files/all_candidate_data.csv')