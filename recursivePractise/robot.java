ArrayList allPaths = new ArrayList();
public void PrintAllPossiblePathsWithObstacles(int M, int N, int[][] obstacles, String path) {
if (obstacles[M][N] == 1)
	return;
else {
	if (M == 0) {
		for (int i = 0; i < N; ++i)
	 	{
			if(obstacles[M][i] == 1)
			return;

			path = "RIGHT " + path;
		}

		System.out.println(path);

		allPaths.add(path);

	} 
	else if (N == 0) {
		for (int i = 0; i < M; ++i)
		{
			if(obstacles[i][N] == 1)
			return;

			path = "DOWN " + path;
		}
			System.out.println(path);
			allPaths.add(path);
} 
else
 {
PrintAllPossiblePathsWithObstacles(M – 1, N, obstacles, "DOWN " + path);
PrintAllPossiblePathsWithObstacles(M, N – 1, obstacles, "RIGHT " + path);
}
}
}