import pandas as pd
import numpy as np
from scipy.sparse import csr_matrix
from sklearn.neighbors import NearestNeighbors

movies = pd.read_csv('movies.csv')
ratings = pd.read_csv('ratings.csv')

final_dataset = pd.merge(ratings, movies, on='movieId')
useritemmatrix = final_dataset.pivot_table(index='userId', columns='title', values='rating', fill_value=0)
sparsity = 1.0 - (np.count_nonzero(useritemmatrix) / float(useritemmatrix.size))
print(f'Sparsity: {sparsity:.2f}')
csr_data = csr_matrix(useritemmatrix.values)
knn = NearestNeighbors(metric='cosine', algorithm='brute', n_neighbors=10, n_jobs=-1)
knn.fit(csr_data)

def movie_rec(nameofmovie, matrix, knn_model, movies_df, n_recs=4):
  
    list = movies_df[movies_df['title'].str.lower().str.contains(nameofmovie.lower())]
    
    if not list.empty:
        movie_idx = list.index[0]
        
        distances, indices = knn_model.kneighbors(matrix[movie_idx], n_neighbors=n_recs+1)
        
        rec_indices = indices.squeeze()[1:]
        
        frame = []
        for idx in rec_indices:
            title = movies_df.iloc[idx]['title']
            dist = distances.squeeze()[idx]
            frame.append({'Title': title, 'Distance': dist})
        
        return pd.DataFrame(frame, columns=['Title', 'Distance'])
    else:
        return f"No movies found matching '{nameofmovie}'."

if __name__ == "__main__":
    nameofmovie = "OK Kanmani"
    recommendations = movie_rec(nameofmovie, csr_data, knn, movies)
    print(f"Recommendations for '{nameofmovie}':")
    print(recommendations)
