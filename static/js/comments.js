$(function() {
    var objectId = parseInt($('#objectId').val());
    var mediaId  = parseInt($('#mediaId').val());
    var lastTime = parseInt($('#lastTime').val());
    var selectedCommentsCount = parseInt($('#selectedCommentsCount').val());

    $("#comments b[data-reply]").each(function() {
        var elem = $(this);
        var addresseeID = elem.data('reply');
        elem.append('<a class="reply text-muted" href="#comment-'+addresseeID+'"><span class="glyphicon icon-undo"></span></a>')
    });

    $("#comments .reply").on('click', function(){
        var body = $("html, body");
        var target = $(this.hash);
        var el = $(this).parent('b').data('reply');
        target = target.length ? target : $('[name=' + this.hash.slice(1) +']');
        if (target.length) {
            body.animate({
                scrollTop: target.offset().top - 20
            }, 1000, function() {
                $(".comment-row[data-id='"+el+"']").addClass("animated flash");
            });
          return false;
        }
    });

  function getSelectedText() {
    if (window.getSelection) {
        return window.getSelection().toString();
    } else if (document.selection) {
        return document.selection.createRange().text;
    }
    return '';
  }

  function markSelection(author) {
    var markerTextChar = "\ufeff";
    var markerTextCharEntity = "&#xfeff;";
    var markerEl, markerId = "sel_" + new Date().getTime() + "_" + Math.random().toString().substr(2);
    var selectionEl;
    var sel, range;
    if (document.selection && document.selection.createRange) {
        range = document.selection.createRange().duplicate();
        range.collapse(false);
        range.pasteHTML('<span id="' + markerId + '" style="position: relative;">' + markerTextCharEntity + '</span>');
        markerEl = document.getElementById(markerId);
    } else if (window.getSelection) {
        sel = window.getSelection();

        if (sel.getRangeAt) {
            range = sel.getRangeAt(0).cloneRange();
        } else {
            range.setStart(sel.anchorNode, sel.anchorOffset);
            range.setEnd(sel.focusNode, sel.focusOffset);
            if (range.collapsed !== sel.isCollapsed) {
                range.setStart(sel.focusNode, sel.focusOffset);
                range.setEnd(sel.anchorNode, sel.anchorOffset);
            }
        }
        range.collapse(false);
        markerEl = document.createElement("span");
        markerEl.id = markerId;
        markerEl.appendChild( document.createTextNode(markerTextChar) );
        range.insertNode(markerEl);
    }
    if (markerEl) {
        if (!selectionEl) {
            selectionEl = document.createElement("div");
            selectionEl.style.position = "absolute";
            selectionEl.className = "btn btn-xs btn-dark btn-quote";
            selectionEl.id = "citeBtn";
            selectionEl.dataset.author = author;
            document.body.appendChild(selectionEl);
        }
    var obj = markerEl;
    var left = 0, top = 0;
    do {
        left += obj.offsetLeft;
        top += obj.offsetTop;
    } while (obj = obj.offsetParent);
        selectionEl.style.left = left + "px";
        selectionEl.style.top = top + "px";
        markerEl.parentNode.removeChild(markerEl);
    }
  };

  $("body").on("click", "#citeBtn", function() {
    var author = "",
        textarea = $("#text_field_text"),
        quoteText = (getSelectedText());
    if ($(this).data('author') != '') {
      var author = "<b>" +$(this).data('author')+ "</b> написал:\n";
    }
    textarea.val(textarea.val()+ "<blockquote>" + author + quoteText + "</blockquote>\n");
    textarea.focus();
    $(this).remove();
  });

  $('#comments .inner, .article-content').on('mouseup', function(){
    var content = getSelectedText();
    var author = $(this).parents('.comment-row').find('.user-nickname:first').text()
    if (content != "") {
      var coords = markSelection(author);
    }
  });
  $('body').on('mousedown', function(e){
    var container = $("#citeBtn");
    if (!container.is(e.target) && container.has(e.target).length === 0) {
        container.remove();
    }
  });
  $("body").on("click", ".comment-quote", function() {
    var textarea = $("#text_field_text"),
      quoteText = (getSelectedText());
    textarea.val(textarea.val()+ "<blockquote>" + quoteText + "</blockquote>\n");
    textarea.focus();
  });

  //старый елемент редактирования, нужно чтобы нельзя было открывать несколько форм редактирования
  var oldEditCommentRow = null;

  //true пока ajax запрос выполняется
  var isProcess = false;

  if (selectedCommentsCount > 0) {
    $('#commentsAdminPanel').animate({top:0}, 500);
  }


  /**
   * Обновление комментариев без перегрузки страницы
   */
  document.addEventListener('updateComments', function(event) {
    console.log(event.detail);

    var options = event.detail || {};

    if (options.id !== undefined) {
      $('#objectId').val(options.id);
      objectId = parseInt(options.id);
    }

    if (options.count !== undefined) {
      var count = parseInt(options.count),
        commentsBlock = $('#comments');

      $('#commentsCounter').text(count);
      commentsBlock.empty();

      if (count) {
        commentsBlock.html('<span class="glyphicon icon-spinner2 loader-icon"></span>');
        $.ajax({
          type: 'POST',
          dataType: 'json',
          url: '/w/comments/unread.json',
          data: {id_object: objectId, id_media: mediaId},
          success: function(response) {
            if (response.success) {
              commentsBlock.empty();
              commentsBlock.append(response.data.html)
            } else {
              commentsBlock.html(response.message);
            }
          }
        });
      }
    }
  });

  //редактирование
  $('#comments').on('click', '.edit-link', function() {

    if (isProcess) {
      return false;
    }

    isProcess = true;

    //старую форму редактирования закрываем
    if (oldEditCommentRow !== null && oldEditCommentRow.length) {
      oldEditCommentRow.find('.comments-edit').remove();
      oldEditCommentRow.find('div.inner').show();
      oldEditCommentRow.find('.comments-options, .post-controls').show();
    }

    var element = $(this);

    var commentRow = element.parents('.comment-row');
    oldEditCommentRow = commentRow;

    var commentId = parseInt(commentRow.data('id'));
    var commentDiv = commentRow.find('.comments-content div.inner');

    $.ajax({
      type: 'POST',
      dataType: 'json',
      url: '/w/comments/get.json',
      data: {id_comment: commentId},
      success: function(response) {

        if (response.success) {
          commentDiv.hide();
          commentRow.find('.comments-content').append(response.data);
          commentRow.find('.comments-options, .post-controls').hide();
        }
        else {
          alert(response.message);
        }

        isProcess = false;
      },
      error: function() {
        alert('Ошибка отправки данных.');
        isProcess = false;
      }
    });

    return false;
  });

  $('#comments').on('submit', 'form.comments-edit', function() {

    var form = $(this);
    var commentRow = form.parents('.comment-row');

    form.find('.comments-js-error').html('');

    $.ajax({
      type: 'POST',
      dataType: 'json',
      url: '/w/comments/edit.json',
      data: form.serialize(),
      success: function(response){
        if (response.success) {
          form.remove();
          commentRow.find('div.inner').html(response.data).show();
          commentRow.find('.comments-options, .post-controls').show();
        }
        else {
          form.find('.comments-js-error').html(response.message);
        }
      },
      error: function() {
        form.find('.comments-js-error').html('Ошибка отправки данных');
      }
    });

    return false;
  });

  $('#comments').on('click', '.comments-edit button[type=reset]', function() {

    var commentRow = $(this).parents('.comment-row');

    commentRow.find('.comments-edit').remove();
    commentRow.find('div.inner').show();
    commentRow.find('.comments-options, .post-controls').show();

    return false;
  });

  //удаление
  $('#comments').on('click', '.delete-link', function() {

    var element = $(this);
    var commentRow = element.parents('.comment-row');
    var commentId = parseInt(commentRow.data('id'));

    BootstrapDialog.show({
          title: 'Подтвердите действие',
          message: 'Вы уверены, что хотите удалить этот комментарий?',
          buttons: [{
              label: 'Удалить',
              cssClass: 'btn-primary',
              action: function(dialog) {
                $.ajax({
                  type: 'POST',
                  dataType: 'json',
                  url: '/w/comments/delete.json',
                  data: {id_comment: commentId},
                  success: function(response) {
                    if (response.success) {
                      //актуализируем кол-во комментариев
                      var commentCount = parseInt($('#commentsCounter').html());
                      $('#commentsCounter').html(commentCount - 1);

                      commentRow.animate({
                        opacity: 1,
                        height: 0,
                        padding: 0
                      }, 'fast', function(){
                        commentRow.remove();
                      });
                    }
                    else {
                      notification('notice', 'Внимание', response.message);
                    }
                  },
                  error: function() {
                    notification('error', 'Ошибка', 'Сервер не отвечает. Попробуйте повторить позднее.');
                  }
                });
                dialog.close();
              }
          }, {
              label: 'Отмена',
              action: function(dialog) {
                dialog.close();
              }
          }]
        });
    return false;
  });

  //ответить
  $('#comments').on('click', '.reply-link', function() {

    var userName = $(this).parents('.comment-row').find('.user-nickname').html(),
        textarea = $('#commentsPostingArea textarea'),
        sourceID = $(this).parents('.comment-row').data('id');

    textarea.val(textarea.val() + '<b data-reply="'+sourceID+'">' + userName + '</b>\n');
    textarea.focus();

    var textLength = textarea.val().length;
    textarea.get(0).setSelectionRange(textLength, textLength);

    var userId = parseInt($(this).data('user'));

    if (userId) {
      $('<input type="hidden" name="reply_user_ids[]" value="' + userId + '">').appendTo('#commentsPostingArea form');
    }

    return false;
  });

  //оценка
  $('#comments').on('click', '.voting .toggleButton', function(){

    var element = $(this);

    //такая оценка уже поставлена
    if (element.hasClass('active disable')) {
      return;
    }

    var mark = element.hasClass('minus') ? -1 : 1;
    var commentId = parseInt(element.parents('.comment-row').data('id'));

    element.siblings('.toggleButton').removeClass('active disable');
    element.addClass('active disable');

    $.ajax({
      type: 'POST',
      dataType: 'json',
      url: '/w/comments/mark.json',
      data: {id_comment: commentId, mark: mark},
      success: function(response) {

        if (response.success) {

          var rating = response.data;
          var jqScore = element.siblings('.score');
          jqScore.removeClass('positive negative');

          if (rating > 0) {
            jqScore.addClass('positive');
          } else if (rating < 0) {
            jqScore.addClass('negative');
          }

          jqScore.html(Math.abs(rating));
        }
        else {
          notification('error', 'Ошибка', response.message);
        }
      },
      error: function() {
        notification('error', 'Ошибка', 'Сервер не отвечает. Попробуйте повторить позднее.');
      }
    });
  });

  //обновление списка
  $('#commentsReload').on('click', function() {

    if (isProcess) {
      return false;
    }

    isProcess = true;

    $.ajax({
      type: 'POST',
      dataType: 'json',
      url: '/w/comments/unread.json',
      data: {id_object: objectId, id_media: mediaId, time: lastTime},
      success: function(response) {

        if (response.success) {

          //актуализируем кол-во комментариев
          var commentCount = parseInt($('#commentsCounter').html());
          $('#commentsCounter').html(commentCount + response.data.count);

          //актуализируем время последнего обновления
          lastTime = response.data.time;

          //отображаем все новые комментарии
          if (response.data.html) {
            $(response.data.html).appendTo('#comments').hide().fadeIn('fast');
          }
        }
        else {
          alert(response.message);
        }
        isProcess = false;
      },
      error: function() {
        notification('error', 'Ошибка', 'Сервер не отвечает. Попробуйте повторить позднее.');
        isProcess = false;
      }
    });

    return false;
  });

  //добавление комментария
  $('#commentsPostingArea form').on('submit', function() {
    $(this).find('button').addClass( 'working_on' );

    if (isProcess) {
      return false;
    }

    isProcess = true;

    var form = $(this);
    var data = form.serialize();

    //отправляем пометку о времени, с которого нам нужны все новые комментарии
    data += '&time=' + lastTime + '&id_object=' + objectId + '&id_media=' + mediaId;

    $.ajax({
      type: 'POST',
      dataType: 'json',
      url: '/w/comments/add.json',
      data: data,
      success: function(response) {

        if (response.success) {
          $('.comments-add button').removeClass( 'working_on' );
          //обнуляем текст сообщения и ошибки
          form.find('textarea').val('');
          form.find('.comments-js-error').html('');

          //актуализируем кол-во комментариев
          var commentCount = parseInt($('#commentsCounter').html());
          $('#commentsCounter').html(commentCount + response.data.count);

          //актуализируем время последнего обновления
          lastTime = response.data.time;

          //отображаем все новые комментарии
          if (response.data.html) {
            $(response.data.html).appendTo('#comments').hide().fadeIn('fast');
          }

        }
        else {
        $('.comments-add button').removeClass( 'working_on' );
          notification('error', 'Ошибка', response.message)
        }
        isProcess = false;
      },
      error: function() {
        $('.comments-add button').removeClass( 'working_on' );
        notification('error', 'Ошибка', 'Сервер не отвечает. Попробуйте повторить позднее.')
        isProcess = false;
      }
    });

    return false;
  });

  /**
   * @return {Array}
   */
  function getSelectedCommentIds() {

    var commentIds = [];

    $('#comments input:checkbox:checked').each(function() {
      commentIds.push(parseInt(this.value));
    });

    return commentIds;
  }

  //перенос выбранных комментов
  $('#cutSelected').on('click', function() {

    var commentIds = getSelectedCommentIds();

    if (!commentIds.length) {
      notification('error', 'Ошибка', 'Нет выбранных сообщений');
      return;
    }

    $.ajax({
      type: 'POST',
      dataType: 'json',
      url: '/w/comments/multi_select.json',
      data: {id_comment: commentIds},
      success: function(response) {

        if (response.success) {
          $('input:checkbox:checked').prop('checked', false);
          window.location.reload();
        }
        else {
          notification('error', 'Ошибка', response.message);
        }
      },
      error: function() {
        notification('error', 'Ошибка', 'Сервер не отвечает. Попробуйте повторить позднее');
      }
    });

    $('#commentsAdminPanel').animate({top:-80}, 500);
    return false;
  });

  //отмена выделения комментариев
  $('#cancelSelection').on('click', function() {

    $.ajax({
      type: 'POST',
      dataType: 'json',
      url: '/w/comments/cancel_selection.json',
      data: {},
      success: function(response) {

        if (response.success) {
          $('input:checkbox:checked').prop('checked', false);
          window.location.reload();
        }
        else {
           notification('error', 'Ошибка', response.message);

        }
      },
      error: function() {
        notification('error', 'Ошибка', 'Сервер не отвечает. Попробуйте повторить позднее');
      }
    });

    return false;
  });

  //перенос выбранных комментов
  $('#moveSelected').on('click', function() {

    $.ajax({
      type: 'POST',
      dataType: 'json',
      url: '/w/comments/multi_move.json',
      data: {id_object: objectId, id_media: mediaId},
      success: function(response) {

        if (response.success) {
          $('input:checkbox:checked').prop('checked', false);
          window.location.reload();
        }
        else {
          notification('error', 'Ошибка', response.message);
        }
      },
      error: function() {
        notification('error', 'Ошибка', 'Сервер не отвечает. Попробуйте повторить позднее');
      }
    });

    return false;
  });

  //перенос выбранных комментов для топиков
  $('#moveSelectedOnTopic').on('click', function() {

    var commentIds = getSelectedCommentIds();

    if (!commentIds.length) {
      notification('error', 'Ошибка', 'Нет выбранных сообщений');
      return;
    }

    var popupWin = window.open(
      'http://www.playground.ru/adm/forums/move/?from_topic=' + objectId + '&id=' + commentIds.join(','),
      'move',
      'location,width=1000,height=270,top=0,left=0,scrollbars=no'
    );

    popupWin.focus();

    var timer = setInterval(function() {
      if (popupWin.closed) {
        clearInterval(timer);
        window.location.reload();
      }
    }, 100);
  });

  //удаление выбранных комментов
  $('#deleteSelected').on('click', function() {

    var commentIds = getSelectedCommentIds();

    if (!commentIds.length) {
      notification('error', 'Ошибка', 'Нет выбранных сообщений');
      return;
    }

    if (!confirm('Точно удалить ' + commentIds.length + ' сообщений ?')) {
      return false;
    }

    $.ajax({
      type: 'POST',
      dataType: 'json',
      url: '/w/comments/multi_delete.json',
      data: {id_comment: commentIds},
      success: function(response) {

        if (response.success) {
          $('input:checkbox:checked').prop('checked', false);
          window.location.reload();
        }
        else {
          notification('error', 'Ошибка', response.message);
        }
      },
      error: function() {
        notification('error', 'Ошибка', 'Попробуйте повторить позднее');
      }
    });

    return false;
  });

  //выделить/снять выделение для всех комментов
  $('#toggleAll').on('change', function() {
    $('#comments input:checkbox').prop('checked', this.checked);
    if($('.admin-comment').is(':checked')) {
      $('.inner').addClass('active');
      $('#commentsAdminPanel').animate({top:0}, 500);
      $(this).next().find('b').text('Отменить выделение');
    }
    else {
      $('.inner').removeClass('active');
      $('#commentsAdminPanel').animate({top:-80}, 500);
      $(this).next().find('b').text('Выделить все комментарии');
    }
  });

  $('#comments').on('change', '.admin-comment',  function() {
    var currentElement = $(this);
    if(currentElement.is(':checked')){
      currentElement.parent('.inner').addClass('active');
    }
    else {
    currentElement.parent('.inner').removeClass('active');
    }
    if($('.admin-comment').is(':checked')) {
      $('#commentsAdminPanel').animate({top:0}, 500);
    }
    else {
      $('#commentsAdminPanel').animate({top:-80}, 500);
    }

  });

  //редактирование топика
  $(document).on('click', '#moderationTools .edit', function() {

    var e = $(this);
    var id = parseInt(e.data('id'));
    if (!id) {
      return false;
    }

    var popupWin = window.open('http://www.playground.ru/adm/forums/topic/edit/?id='+id, 'pm', 'location,width=1000,height=330,top=0,left=0,scrollbars=no');
    popupWin.focus();

    var timer = setInterval(function() {
      if (popupWin.closed) {
        clearInterval(timer);
        window.location.reload();
      }
    }, 100);

    return false;
  });

  //удаление топика
  $(document).on('click', '#moderationTools .delete', function() {

    var e = $(this);
    var id = parseInt(e.data('id'));
    if (!id) {
      return false;
    }

    if (!confirm('Точно удалить тему?')) {
      return false;
    }

    $.ajax({
      type: 'POST',
      dataType: 'json',
      url: '/json/controller/adm/forums/topic/delete/',
      data: {id: id},
      success: function(response) {
        if (response.success) {
          var chunks = window.location.href.split('/');
          window.location.href = chunks.slice(0, chunks.length - 2).join('/') + '/';
        }
        else {
          notification('error', 'Ошибка', response.message);
        }
      },
      error: function() {
        notification('error', 'Ошибка', 'Ошибка отправки данных.');
      }
    });

    return false;
  });
});
