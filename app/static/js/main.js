var s, app = {
    settings : {
        jpm: {}
    },
    init: function() {
        //Global settings
        s = this.settings;

        // initalize
        this.initalizers();
        this.bindUiActions();
    },
    bindUiActions: function (){
        // Should include all JS user interactions
        var self = this;

        $('.select-posts,.select-categories').on('click', function () {
            self.homePostsCatSwitch();
        });

        $('.social-icon').on('click', function(){
            self.socialIconClick( $(this) );
        });

    },
    initalizers: function (){
        // Initalize any plugins for functions when page loads

        // JPanel Menu Plugin -
        this.jpm();

        // Fast Click for Mobile - removes 300ms delay - https://github.com/ftlabs/fastclick
        FastClick.attach(document.body);

        // Add Bg colour from JS so jPanel has time to initalize
        $('body').css({"background-color":"#333337"});
    },
    homePostsCatSwitch: function(){
        // Toggles between showing the categories and posts on the homepage
        $('.home-page-posts').toggleClass("hide");
        $('.home-page-categories').toggleClass("hide");
        $('.select-posts').toggleClass("active");
        $('.select-categories').toggleClass("active");
        $('.home-footer').toggleClass("hide");
    },
    socialIconClick: function(el) {
        // Post page social Icons
        // When Clicked pop up a share dialog

        var platform = el.data('platform');
        var message = el.data('message');
        var url = el.data('url');

        if (platform == 'mail'){
            // Let mail use default browser behaviour
            return true;
        } else {
            this.popItUp(platform, message, url);
            return false;
        }
    },
    popItUp : function (platform, message, url) {
        // Create the popup with the correct location URL for sharing
        var popUrl,
            newWindow;

        if( platform == 'twitter'){
            popUrl = 'http://twitter.com/home?status=' + encodeURI(message) + '+' + url;

        } else if(platform == 'facebook'){
            popUrl = 'http://www.facebook.com/share.php?u' + url + '&amp;title=' + encodeURI(message);
        }
        newWindow = window.open(popUrl,'name','height=500,width=600');
        if (window.focus) { newWindow.focus(); }
        return false;

    },
    jpm: function(){
        // Off Screen Navigation Plugin

        s.jpm = $.jPanelMenu({
            menu : '#menu-target',
            trigger: '.menu-trigger',
            animated: false,
            beforeOpen : ( function() {
                if (matchMedia('only screen and (min-width: 992px)').matches) {
                    $('.sidebar').css("left", "250px");
                }
            }),
            beforeClose : ( function() {
                $('.sidebar').css("left", "0");
                $('.writer-icon, .side-writer-icon').removeClass("fadeOutUp");
            })
        });

        s.jpm.on();
    }
};

$(document).ready(function(){
    app.init();

    // Contact Validator
    $('#contact_form').bootstrapValidator({
    feedbackIcons: {
        valid: 'glyphicon glyphicon-ok',
        invalid: 'glyphicon glyphicon-remove',
        validating: 'glyphicon glyphicon-refresh'
    },
    fields: {
        name: {
            validators: {
                stringLength: {
                    min: 2,
                    max: 50
                },
                notEmpty: {
                    message: 'Please supply your full name'
                }
            }
        },
        email: {
            validators: {
                notEmpty: {
                    message: 'Please supply your email address'
                },
                regexp: {
                    regexp: '^[^@\\s]+@([^@\\s]+\\.)+[^@\\s]+$',
                    message: 'Please supply a valid email address'
                }
            }
        },
        phone: {
            enabled: false,
            validators: {
                notEmpty: {
                    message: 'Please supply your phone number'
                },
                phone: {
                    country: 'US',
                    message: 'Please supply a valid phone number with area code'
                }
            }
        },
        company: {
            validators: {
                stringLength: {
                    min: 2,
                    max: 50,
                    message: 'Please enter at least 2 characters and no more than 50'
                },
                notEmpty: {
                    message: 'Please supply a your company'
                }
            }
        },
        message: {
            validators: {
                stringLength: {
                    min: 10,
                    max: 200,
                    message: 'Please enter at least 10 characters and no more than 200'
                },
                notEmpty: {
                    message: 'Please supply a your message'
                }
            }
        }
    }
    })
    .on('keyup', '[name="email"], [name="phone"]', function(e) {
        var email = $('#contact_form').find('[name="email"]').val(),
            phone = $('#contact_form').find('[name="phone"]').val(),
            fv = $('#contact_form').data('bootstrapValidator');
            switch ($(this).attr('name')) {
            // User is focusing the email field
            case 'email':
                fv.enableFieldValidators('phone', email === '').revalidateField('phone');

                if (email && fv.getOptions('email', null, 'enabled') === false) {
                    fv.enableFieldValidators('email', true).revalidateField('email');
                } else if (email === '' && phone !== '') {
                    fv.enableFieldValidators('email', false).revalidateField('email');
                }
                break;

            // User is focusing the phone field
            case 'phone':
                fv.enableFieldValidators('phone', phone !== '').revalidateField('phone');

                if (phone === '') {
                    fv.enableFieldValidators('email', true).revalidateField('email');
                } else if (email === '') {
                    fv.enableFieldValidators('email', false).revalidateField('email');
                }
                if (phone && email === '' && fv.getOptions('phone', null, 'enabled') === false) {
                    fv.enableFieldValidators('phone', true).revalidateField('phone');
                }
                break;

            default:
                break;
        }
    })
    .on('success.form.bv', function(e) {
         $('#success_message').show();
         setTimeout(function(){
            $('#success_message').hide();
         }, 4000);
        // Prevent form submission
        e.preventDefault();
        // Get the form instance
        var $form = $(e.target);
        // Get the BootstrapValidator instance
        // var bv = $form.data('bootstrapValidator');
        // Use Ajax to submit form data
        $.post("/contact/", $form.serialize(), function (result) {
            console.log(result);
        });
        // Clear form after submit
        $('#contact_form').bootstrapValidator('resetForm', true);
    });
});