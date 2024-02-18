
const suppDoublon = (word) => {
    console.log(word)
    var mots = word.split('');
    console.log(mots)

    var obj = {};
    var rep = "";

    for (let index = 0; index < mots.length; index++) {
        if(obj[mots[index]]){
            obj[mots[index]] += 1
        }
        else{
            obj[mots[index]] = 1
        }
        console.log(obj);
    }

    console.log(Object.keys(obj))
    
    for (const key in obj) {
       if(obj[key] === 1){
        rep += key
       }
    }
    return rep;
}

console.log(suppDoublon('annapi'));



// Ex : Ann, => A 
// Ex