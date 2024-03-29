from sklearn.cluster import KMeans
#from spherecluster import VonMisesFisherMixture, SphericalKMeans
#from soyclustering import SphericalKMeans
#from coclust.clustering.spherical_kmeans import SphericalKmeans
from torchclust.utils.spherical_kmeans import SphericalKmeans
import torch


def get_clusters(x: torch.Tensor,
                 n_clusters: int,
                 kind: str = "kmeans") -> torch.Tensor:
        if kind == "kmeans":
            kmeans = KMeans(n_clusters=n_clusters, n_init=100)
            _ = kmeans.fit_predict(x.detach().numpy())
            return torch.Tensor(kmeans.cluster_centers_), torch.Tensor(kmeans.labels_)


        elif kind == "movMF-soft":
            # spharical kmeans
            vmf_soft = VonMisesFisherMixture(n_clusters=n_clusters, posterior_type='soft')
            vmf_soft.fit(x.detach().numpy())
            return torch.Tensor(vmf_soft.cluster_centers_), torch.Tensor(vmf_soft.predict(x))

        elif kind == "rand-SphericalKmeans":
            skmeans = SphericalKmeans(n_clusters=n_clusters,
                                      max_iter=100,
                                      n_init=50)
            skmeans.fit(x.detach().numpy())
            return torch.Tensor(skmeans.centers), torch.Tensor(skmeans.labels_)