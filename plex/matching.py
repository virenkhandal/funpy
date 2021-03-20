def match(students, employers, num_clusters):
    from clustering import cluster; import pandas as pd; import numpy as np; import scipy; from scipy.spatial import distance; from sklearn.metrics.pairwise import cosine_distances, cosine_similarity

    clusteredEmployers = cluster(employers, num_clusters)

    clusteredStudents = cluster(students, num_clusters)

    for index, employer in clusteredEmployers.iterrows():
        cluster = employer['Cluster #']
        filtered_students = clusteredStudents[clusteredStudents['Cluster #'] == cluster]
        best_student = ""
        most_similar = -1
        for index, student in filtered_students.iterrows():
            arr = employer.values.tolist()
            student_arr = student.values.tolist()
            employer_values = np.array(arr[1:])
            student_values = np.array(student_arr[1:])
            cosine = cosine_similarity(employer_values.reshape(1, -1), student_values.reshape(1, -1))[0][0]
            if cosine > most_similar:
                most_similar = cosine
                best_student = student_arr[0]
        print("The best student for " + employer['Company Name'] + " is " + best_student + ". This student has a " + str(round(most_similar * 100, 1)) + "% similarity to the company's preferences.")


if __name__ == "__main__":
    import pandas as pd; import boto3
    client = boto3.client('s3')
    path = "s3://misc.funpy/"
    students = path + "Student_Registration.csv"
    employers = path + "CORRECT_Employer_Full_Registration.csv"
    num_clusters = int(input("Enter number of clusters you wish to cluster into: "))
    match(students, employers, num_clusters)