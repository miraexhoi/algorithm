function solution(arr, queries) {
    var answer = [...arr];
    for(let i=0; i<queries.length; i++){
        let box = answer[queries[i][0]]
        answer[queries[i][0]]=answer[queries[i][1]];
        answer[queries[i][1]]=box 
    }
    return answer;
}

console.log(solution([0, 1, 2, 3, 4],[[0, 3],[1, 2],[1, 4]]	))