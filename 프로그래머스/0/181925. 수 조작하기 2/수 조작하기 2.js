function solution(log) {
    let result = "";
    for(let i=0; i<log.length; i++){
        const n = log[i+1]-log[i];
        switch(n){
            case 1: result += "w"; break;
            case -1: result += "s"; break;
            case 10: result += "d"; break;    
            case -10: result += "a"; break;
        }    
    }
    return result;
}