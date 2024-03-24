function openBlog(url) {
  window.open(url, '_blank');
}

function updateLikes(blogId) {
  const likeCounter = document.getElementById(`likeCounter${blogId}`);
  let likes = parseInt(localStorage.getItem(`likes${blogId}`)) || 0;
  likes++;
  localStorage.setItem(`likes${blogId}`, likes);
  likeCounter.textContent = `Likes: ${likes}`;

  broadcastUpdate({ type: 'like', blogId, likes });
}

function addComment(blogId) {
  const commentInput = document.getElementById(`commentInput${blogId}`);
  const commentsList = document.getElementById(`commentsList${blogId}`);
  const commentText = commentInput.value.trim();

  if (commentText !== '') {
    const commentItem = document.createElement('li');
    commentItem.textContent = `${commentsList.childElementCount + 1}. ${commentText}`;
    commentsList.appendChild(commentItem);

    const savedComments = JSON.parse(localStorage.getItem(`comments${blogId}`)) || [];
    savedComments.push(commentText);
    localStorage.setItem(`comments${blogId}`, JSON.stringify(savedComments));

    commentInput.value = ''; // Clear the input field after adding the comment

    broadcastUpdate({ type: 'comment', blogId, comment: commentText });
  }
}

function displayComments(commentsList, comments) {
  commentsList.innerHTML = '';
  comments.forEach((comment, index) => {
    const li = document.createElement('li');
    li.textContent = `${index + 1}. ${comment}`;
    commentsList.appendChild(li);
  });
}

function loadLikesAndComments(blogId) {
  const likeCounter = document.getElementById(`likeCounter${blogId}`);
  const commentsList = document.getElementById(`commentsList${blogId}`);
  const commentInput = document.getElementById(`commentInput${blogId}`);

  // Load likes
  let likes = parseInt(localStorage.getItem(`likes${blogId}`)) || 0;
  likeCounter.textContent = `Likes: ${likes}`;

  // Load comments
  let comments = JSON.parse(localStorage.getItem(`comments${blogId}`)) || [];
  displayComments(commentsList, comments);

  commentInput.addEventListener('keyup', function (event) {
    if (event.key === 'Enter') {
      addComment(blogId);
    }
  });
}

// Load existing likes and comments on page load
document.addEventListener('DOMContentLoaded', () => {
  for (let i = 1; i <= 2; i++) {
    loadLikesAndComments(i);
  }
});

// Send updates to other open windows
function broadcastUpdate(update) {
  localStorage.setItem('blogUpdate', JSON.stringify(update));
}

// Listen for updates from other open windows
window.addEventListener('storage', function (event) {
  if (event.key === 'blogUpdate') {
    const update = JSON.parse(event.newValue);
    if (update) {
      if (update.type === 'like') {
        const likeCounter = document.getElementById(`likeCounter${update.blogId}`);
        likeCounter.textContent = `Likes: ${update.likes}`;
      } else if (update.type === 'comment') {
        const commentsList = document.getElementById(`commentsList${update.blogId}`);
        const commentItem = document.createElement('li');
        commentItem.textContent = `${commentsList.childElementCount + 1}. ${update.comment}`;
        commentsList.appendChild(commentItem);
      }
    }
  }
});

// Save new comments before unloading
window.addEventListener('unload', function () {
  for (let i = 1; i <= 2; i++) {
    addComment(i);
  }
});
