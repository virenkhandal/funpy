import pandas as pd
from termcolor import colored
import warnings

warnings.filterwarnings("ignore")

from round1 import round1_filter
from round2 import round2_cluster, match_skills
from round3 import cleanup, match_socials
from utils import pretty_print, optimize_skills, plot_evaluation, find_num_clusters

def match(students, employers):
    students = pd.read_csv(students)
    employers = pd.read_csv(employers)

    employers = employers.rename(columns={'Company Name': 'Name', 'Majors and Minors (check all that apply)':'Majors/Minors', 'Identify only 3':'Social Causes', 'Citizenship (check all that apply)':'Citizenship'})
    students = students.rename(columns={'Best email to reach you':'Name', 'Select your major and minor (check all that apply)':'Majors/Minors', 'What social causes matter to  you? Employers and students identify causes that matter to them.(Choose up to 3).  Check out our Get Involved page on Intern Pursuit for more information: https://www.internpursuit.tech/get-involved':'Social Causes'})
    for i in range(len(employers.index)):

        # obtain i-th employer from dataframe
        curr = employers.iloc[[i]]

        # perform filtering on all students based on criteria of i-th employer
        filtered = round1_filter(students, curr)
        text = "Students remaining after first round: " + str(len(filtered))
        print(colored(text, "magenta"))
        # filtered = students
        # create dataframe with filtered students and i-th employer
        appended = filtered.append(curr)

        # find optimal number of clusters for appended dataframe
        s_score, db_score = optimize_skills(appended)
        s_clusters = find_num_clusters(plot_evaluation(s_score))
        db_clusters = find_num_clusters(plot_evaluation(db_score))

        # perform clustering on appended using both of the optimized cluster scores, use appended dataframe because we need apply a bonus weight if student and employer's clusters match
        s_clustered = round2_cluster(appended, s_clusters)
        db_clustered = round2_cluster(appended, db_clusters)

        # get list of top 10-12 candidates as a list of tuples (x, y) where x is the candidate's email address and y is their similarity score
        s_optimal_matchings = match_skills(s_clustered)
        db_optimal_matchings = match_skills(db_clustered)
        text = "Students remaining after second round: " + str(len(s_optimal_matchings))
        print(colored(text, "magenta"))

        # cleanup all dataframes and get new dataframe which includes candidate's email, similarity score, and social causes columns
        s_cleaned_up = cleanup(filtered, s_clustered, s_optimal_matchings)
        db_cleaned_up = cleanup(filtered, db_clustered, db_optimal_matchings)

        # return list of top 3-5 candidates based on social clustering
        s_final = match_socials(s_cleaned_up, curr)
        db_final = match_socials(db_cleaned_up, curr)
        
        # pretty print top candidates for current employer
        output = pretty_print(s_final, curr)
        # pretty_print(db_final)
    return

if __name__ == "__main__":
    # student_file = input("Enter hte name of the student csv file (with path): ")
    # employer_file = input("Enter the name of the employer csv file (with path): ")
    
    match('students.csv', 'employers.csv')