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
