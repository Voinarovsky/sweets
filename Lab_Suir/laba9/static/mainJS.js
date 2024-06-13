function updateFeedback1(el){
    feedback_id = el.value
    fetch('/estimation1/' + feedback_id,
        {method: 'patch',
        headers: {'Content-Type': 'application/json'},
        body: JSON.stringify({'estimation1': el.checked})
        })
}
function updateFeedback2(el){
    feedback_id = el.value
    fetch('/estimation2/' + feedback_id,
        {method: 'patch',
        headers: {'Content-Type': 'application/json'},
        body: JSON.stringify({'estimation2': el.checked})
        })
}
function updateFeedback3(el){
    feedback_id = el.value
    fetch('/estimation3/' + feedback_id,
        {method: 'patch',
        headers: {'Content-Type': 'application/json'},
        body: JSON.stringify({'estimation3': el.checked})
        })
}
function createFeedback(){
    console.log('Create')
    let response = document.getElementById('response').value
    let estimation1 = document.getElementById('estimation1').value
    let estimation2 = document.getElementById('estimation2').value
    let estimation3 = document.getElementById('estimation3').value

    fetch('/feedback',{
        method: 'post',
        headers: {'Content-Type': 'application/json'},
        body: JSON.stringify({'response': response || 'Без отзыва', 'estimation1': false, 'estimation2': false, 'estimation3': false })
    })
}
