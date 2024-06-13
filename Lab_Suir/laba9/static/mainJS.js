function updateFeedback(el){
    feedback_id = el.value
    fetch('/estimation/' + feedback_id,
        {method: 'patch',
        headers: {'Content-Type': 'application/json'},
        body: JSON.stringify({'estimation': el.checked})
        })
}
function createFeedback(){
    console.log('Create')
    let response = document.getElementById('response').value
    let estimation = document.getElementById('estimation').value

    fetch('/feedback',{
        method: 'post',
        headers: {'Content-Type': 'application/json'},
        body: JSON.stringify({'response': response || 'Без отзыва', 'estimation': estimation})
    })
}
