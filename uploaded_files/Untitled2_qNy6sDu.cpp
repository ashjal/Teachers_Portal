#include<bits/stdc++.h>
using namespace std;
#define max 100003
long long a[30000],n,q,val[5000][5000]={{0}},pro[30000]={0};

int main()
{
	freopen("in1.txt","r",stdin);
	int k;
	scanf("%lld",&n);
	for(int i=0;i<n;i++)
	{
		scanf("%lld",&a[i]);
	}
	for(int i=0;i<n;i++)
	{
		val[i][i]=a[i];
	}
	for(int i=n-2;i>=0;i--)
	{
		a[i]+=a[i+1];
	}
	int j;
	for(int i=0;i<n-1;i++)
	{
		j=0;
		for(int k=i;k<n-1;k++,j++)
		{
			long long temp=(val[j][j]*val[j+1][k+1])%max;;
			val[j][k+1]=temp;
		}
	}
	//cout<<endl;
	//for(int i=0;i<n;i++)
	{
		//for(int j=0;j<n;j++)
	//	cout<<val[i][j]<<" ";
		
	//	cout<<endl; 
	}	
	long long temp=0;
	for(int i=0;i<n-1;i++)
	{
		temp=0;
		j=0;
		for(int k=i;k<n-1;k++,j++)
		{
			temp+=a[k+1]*val[j][k];;
			//pro[i+1]%=max;
			temp%=max;
			//cout<<val[j][k]<<" "<<a[k+1]<<endl;
		}
		pro[i+1]=temp;
	}
	
	cin>>q;
	while(q--)
	{
		cin>>k;
		if(k==1)
		cout<<a[0]<<endl;
		else
		cout<<pro[k-1]<<endl;
	}
}
