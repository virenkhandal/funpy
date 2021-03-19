def match(students, employers, num_clusters):
    from clustering import cluster; import pandas as pd; import numpy as np; import scipy; from scipy.spatial import distance

    clusteredEmployers = cluster(employers, num_clusters)

    clusteredStudents = cluster(students, num_clusters)

    for index, employer in clusteredEmployers.iterrows():
        cluster = employer['Cluster #']
        filtered_students = clusteredStudents[clusteredStudents['Cluster #'] == cluster]
        best_student = ""
        lowest_dist = 100000
        for index, student in filtered_students.iterrows():
            arr = employer.values.tolist()
            student_arr = student.values.tolist()
            employer_values = arr[1:]
            student_values = student_arr[1:]
            distance = scipy.spatial.distance.euclidean(employer_values, student_values)
            if distance < lowest_dist:
                lowest_dist= distance
                best_student = student_arr[0]
        print("The best student for " + employer['Company Name'] + " is " + best_student + ". This student has a " + str(round(100 - lowest_dist, 1)) + "% similarity to the company's preferences.")


if __name__ == "__main__":
    students = input("Enter students csv file name (with route if nested): ")
    employers = input("Enter employers csv file name (with route if nested): ")
    num_clusters = int(input("Enter number of clusters you wish to cluster into: "))
    match(students, employers, num_clusters)