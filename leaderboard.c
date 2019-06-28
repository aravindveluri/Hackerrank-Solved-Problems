#include <stdio.h>
struct sco {
        int points;
	int rank;
};
int f(struct sco v1[], struct sco v2[], int ch1, int ch2, int *ranke){
	if(v1[ch1].points > v2[ch2].points){
		v1[ch1].rank = v2[ch2].rank;
		*ranke = v2[ch2].rank;
		v2[ch2].rank = v2[ch2].rank-1;
	}
}

int main(void) {
	//struct sco {
	//	int points;
	//	int rank;
	//}
			
	int n,m;
	struct sco s[n];
	struct sco a[m];
	int rnk = 1;
	scanf("%d",&n);
	scanf("%d",&(s[0].points));
	s[0].rank = 1;
	for(int i=1; i<n;i++){
		scanf("%d",&(s[i].points));
		if(s[i].points == s[i-1].points){
			s[i].rank = s[i-1].rank;
		}
		else{
			s[i].rank = (s[i-1].rank)+1;
			rnk++;
		}
		
	}
	scanf("%d",&m);
	for(int i=0; i<n;i++){
		scanf("%d",&(a[i].points));
	}
	int start = s[0].points;
	int c=1;
	for(int i=0; i<m;i++){
		int ranker = 1;
		for(int j=0; j<n;j++){
			/*if(a[i].points > s[j].points){
				a[i].rank = s[j].rank;
				ranker = s[j].rank;
				s[j].rank = ranker-1;
			}*/
			f(a, s, m, n, &ranker);
			if(a[i].points < s[j].points){
				a[i].rank = s[j].rank + 1;
				ranker = s[j].rank + 1;
			}
			if(a[i].points == s[j].points){
				a[i].rank = s[j].rank;
				ranker = s[j].rank;
			}
		}
		printf("%d\n", ranker);
	}
	return 0;
}

