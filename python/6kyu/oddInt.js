function findOdd(a) {
    let evenOrOddObj = {};
    a.forEach(elem => elem in evenOrOddObj ? evenOrOddObj[elem]++ : evenOrOddObj[elem] = 1);
    for(let key in evenOrOddObj) {
        if(evenOrOddObj[key] % 2 > 0) return parseInt(key);
    }
    return 0;
}

function longestConsec (strarr, k) {
    if(k <= 0 || k > strarr.length) return "";
    let longest = "";
    for(let i = 0; i < strarr.length; i++) {
      let subArr = strarr.slice(i, i+k).join("");
      subArr.length > longest.length ? longest = subArr : null;
    }
    return longest;
}
