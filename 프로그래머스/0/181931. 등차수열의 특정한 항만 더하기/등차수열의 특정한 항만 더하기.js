function solution(a, d, included) {
    var answer = 0;
    for(let i = 0; i < included.length; i++) {
        if(included[i]) {
            answer += (a + (d * i))
        }
    }
    return answer;
}