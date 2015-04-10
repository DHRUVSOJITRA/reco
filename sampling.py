import pandas as pd

# calculate stastistical information on small dataset
def recompute_frame(ldf):
    """
    takes a dataframe ldf, makes a copy of it, and returns the copy
    with all averages and review counts recomputed
    this is used when a frame is subsetted.
    """
    ldfu=ldf.groupby('user_id')
    ldfb=ldf.groupby('business_id')
    user_avg=ldfu.stars.mean()
    user_review_count=ldfu.review_id.count()
    business_avg=ldfb.stars.mean()
    business_review_count=ldfb.review_id.count()
    nldf=ldf.copy()
    nldf.set_index(['business_id'], inplace=True)
    nldf['business_avg']=business_avg
    nldf['business_review_count']=business_review_count
    nldf.reset_index(inplace=True)
    nldf.set_index(['user_id'], inplace=True)
    nldf['user_avg']=user_avg
    nldf['user_review_count']=user_review_count
    nldf.reset_index(inplace=True)
    return nldf


fulldf = pd.read_csv("/home/dhruv/Desktop/cmpe239/hotel_reco/bigdf.csv")
smallidf=fulldf[(fulldf.user_review_count > 60) & (fulldf.business_review_count > 150)]
smalldf=recompute_frame(smallidf)

# extract necessary information and store them for whole and smaller dataset
subsetoffull=fulldf[['user_id','business_id', 'stars','business_avg','user_avg']]
subsetoffull.to_csv("subset-full.csv", index=False, header=False)

subsetofsmall=smalldf[['user_id','business_id', 'stars','business_avg','user_avg']]
subsetofsmall.to_csv("subset-small.csv", index=False, header=False)
