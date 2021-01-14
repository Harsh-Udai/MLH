
let ptag = document.getElementById('data-wrap')


const data = fetch('/data').then((result)=>{
    result.json().then((data)=>{
        console.log((data.data).length);

        if(data.data.length == 0){
            ptag.textContent = "No To-Do's"
        }
        else{
            const final = data.data;
            final.forEach(element => {
                ptag.innerHTML += ('<p>'+element)
            });
        }
    })
});


document.querySelector('button').addEventListener('click',(ele)=>{
    ele.preventDefault();

    const inputData = document.getElementById('inputData').value;
    document.getElementById('inputData').value=''
    // console.log(inputData);
    fetch('/data_main?todo='+inputData+'').then((result)=>{
        result.json().then((data)=>{
            // console.log((data.data).length);
            ptag.innerHTML="";
            if(data.data.length == 0){
                ptag.textContent = "No To-Do's"
            }
            else{
                const final = data.data;
                final.forEach(element => {
                    ptag.innerHTML += ('<p>'+element)
                });
            }
        })
    });
})

document.getElementById('data-wrap').onclick= ()=>{
    let val = document.getElementById('data-wrap').textContent;
    const wildCard = "No To-Do's";

    if(val !== wildCard){
        fetch('/delete?todo='+val).then((result)=>{
            result.json().then((data)=>{
                // console.log((data.data).length);
                ptag.innerHTML="";
                if(data.data.length == 0){
                    ptag.textContent = "No To-Do's"
                }
                else{
                    const final = data.data;
                    final.forEach(element => {
                        ptag.innerHTML += ('<p>'+element)
                    });
                }
            })
        });
    }
}