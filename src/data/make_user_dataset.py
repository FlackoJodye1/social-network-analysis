# User-Data

# Create a dataset of Users containing all relevant attributes to assess assortative mixing
import pandas as pd
from pathlib import Path

# Load all Data
INPUT_DIR = Path("../../data/raw/")
OUTPUT_DIR = Path("../../data/processed/")
filename_following = "Following_Ignoring_Relationships_01052019_31052019.csv"
filename_votes_first = "Votes_01052019_15052019.csv"
filename_votes_second = "Votes_16052019_31052019.csv"
filename_postings_first = "Postings_01052019_15052019.csv"
filename_postings_second = "Postings_01052019_15052019.csv"

relationships = pd.read_csv(INPUT_DIR / filename_following, sep=';')
votes_first = pd.read_csv(INPUT_DIR / filename_votes_first, sep=';')
votes_second = pd.read_csv(INPUT_DIR / filename_votes_second, sep=';')

postings_first = pd.read_csv(INPUT_DIR / filename_postings_first, sep=';')
postings_second = pd.read_csv(INPUT_DIR / filename_postings_second, sep=';')

# Filter the data for relevant attributes

# Relationships
relationships = relationships.drop(columns=['ID_CommunityConnectionType'])

unique_user_ids_following = pd.unique(relationships[['ID_CommunityIdentity', 'ID_CommunityIdentityConnectedTo']].values.ravel('K'))

# Votes
votes = pd.concat([votes_first, votes_second])
votes = votes.drop(columns=["ID_Posting", "VotePositive", "VoteNegative", "VoteCreatedAt", "UserCommunityName"])
unique_user_ids_votes = pd.unique(votes["ID_CommunityIdentity"])

# Postings
postings = pd.concat([postings_first, postings_second])
postings = postings.drop(columns=["ID_Posting", "ID_Article", "PostingHeadline", "PostingComment", "PostingCreatedAt", "ArticlePublishingDate", "ArticleRessortName", "ArticleTitle", "ArticleChannel", "UserCommunityName", "ID_Posting_Parent"])
unique_user_ids_postings = pd.unique(postings["ID_CommunityIdentity"])

# Combine
votes_and_postings = pd.concat([votes, postings])
votes_and_postings = votes_and_postings.drop_duplicates(subset="ID_CommunityIdentity")
votes_and_postings = votes_and_postings.reset_index(drop=True)

users = pd.merge(pd.DataFrame(unique_user_ids_following, columns=['ID_CommunityIdentity']), votes_and_postings, on='ID_CommunityIdentity', how='left')

users['UserCreatedAt'] = pd.to_datetime(users['UserCreatedAt'])
users['UserCreatedAt'] = users['UserCreatedAt'].dt.date
print(f"Created User-Dataset of length {len(users)}")
print(users.isnull().sum() / len(users))

filename_output = "user.csv"
users.to_csv(OUTPUT_DIR / filename_output, index=False)
