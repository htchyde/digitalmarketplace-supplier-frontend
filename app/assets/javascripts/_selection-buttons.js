;// assumes show-hide-content.js is inserted above (which has no trailing semi-colon)
(function(GOVUK, GDM) {

  GDM.selectionButtons = function() {

    if (!GOVUK.SelectionButtons) return;

    new GOVUK.SelectionButtons('.selection-button input', {
      'focusedClass' : 'selection-button-focused',
      'selectedClass' : 'selection-button-selected'
    });

    new GOVUK.ShowHideContent().init();

  };

  GOVUK.GDM = GDM;

}).apply(this, [GOVUK||{}, GOVUK.GDM||{}]);