import pandas as pd

def cleanup(filtered, clustered, matchings):
    df = pd.DataFrame(columns=["Name", "Scores", "Social Causes"])
    for i in range(len(matchings)):
        person = matchings[i]
        score, name = person[0], person[1]
        social_causes = filtered[filtered['Name'] == name]['Social Causes']
        df.loc[len(df)] = [name, score, social_causes]
    
    return df

def match_socials(dataframe, curr):
    curr = curr[['Name', 'Social Causes']]
    employer_social = set(curr['Social Causes'].values[0].split(';'))
    df = pd.DataFrame(columns=["Name", "Final Score"])
    for index, row in dataframe.iterrows():
        if len(row[2].values) > 0:
            social = row[2].values[0]
            if isinstance(social, str):
                causes = social.split(';')
                overlap = len(list(employer_social.intersection(causes)))/3
            else:
                overlap = 0
            updated_score = (row[1] * 0.75) + (overlap * 0.25)
            df.loc[len(df)] = [row[0], updated_score]
    return df