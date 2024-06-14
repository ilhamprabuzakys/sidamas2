
L.HtmlOverlay = L.Layer.extend({
    /*
    en gros une copie modifiÃ©e de ImageOverlay
    avec quand-mÃªme pas mal de soucis avec le scale du html
    qui ne suit pas tout seul...
    */
  
    options: {
      interactive: false,
      zIndex: 1,
      className: '',
      idName: '',
      zoom: '' // le niveau de zoom ou la div est affichÃ© Ã  l'Ã©chelle 1
    },
  
    initialize: function (code, coords, options) { // (String, LatLngBounds, Object)
      this._code = code; // code brut
  
      // astuce : on fournit une seule coordonnÃ©e
      // this._bounds = L.latLngBounds(bounds);
      this._bounds = L.latLngBounds([coords, coords]);
  
      L.setOptions(this, options);
  
      // scale de dÃ©part 1, au niveau de zoom actuel...
      this._scale = 1;
    },
  
    // precious tool for moving around the htmlOverlay
    // with only one set of coords
    setLatLng: function(coords){
      this.setBounds(L.latLngBounds([coords, coords]));
    },
  
    onAdd: function(){
      if(!this._dom){
        this._initDom();
      }
  
      if (this.options.interactive) {
        L.DomUtil.addClass(this._dom, 'leaflet-interactive');
        this.addInteractiveTarget(this._dom);
      }
  
      this.getPane().appendChild(this._dom);
      this._reset();
  
      // zoom natif courant si pas indiquÃ©
      if(this.options.zoom === '') this.options.zoom = this._map.getZoom();
  
      // ok, par rapport au zoom natif il faudrait un scale de dÃ©part de...
      this._scale = this._map.getZoomScale(this._map.getZoom(), this.options.zoom);
  
      // on applique donc ce coef dÃ¨s maintenant, Ã§a servira de base de calcul par la suite
      this._inner.style.transform = "scale("+this._scale+")";
  
      // important : pdt le zoom il y a un scale css, 
      // mais Ã  la fin du zoom il est retirÃ©
      // il faut le rÃ©tablir sur le contenu html seulement
      this._map.on('zoomend', this._rescaleInnerHtml, this);
    },
    
    _rescaleInnerHtml(){ // Ã  la fin du zoom on applique un scale Ã  l'intÃ©rieur
      this._scale *= this._rescale;
      this._inner.style.transform = "scale("+this._scale+")";
    },
  
    onRemove: function () {
      // retirer l'Ã©coute du zoom
      this._map.off('zoomend', this._rescaleInnerHtml, this);
  
      L.DomUtil.remove(this._dom);
      if (this.options.interactive) {
        this.removeInteractiveTarget(this._dom);
      }
    },
  
    _initDom: function(){
      // crea d'une div qui va contenir notre code html
      var dom = L.DomUtil.create('div', 'leaflet-html-layer');
  
      // Ã§a c'est comme ImageOverlay
      if (this._zoomAnimated) { L.DomUtil.addClass(dom, 'leaflet-zoom-animated'); }
      if (this.options.className) { L.DomUtil.addClass(dom, this.options.className); }
  
      dom.onselectstart = function(){ return false; };
      dom.onmousemove = function(){ return false; };
  
      if (this.options.zIndex) {
        this._updateZIndex();
      }
  
      // ok c'est lÃ  qu'on injecte le code html
      dom.innerHTML = this._code;
  
      this._dom = dom;
      this._dom.style.position = "relative";
  
      // avec des rÃ©glages css pour Ã©viter des soucis...
      this._inner = this._dom.childNodes[0]; // un seul noeud
      this._inner.style.position = "absolute";
      this._inner.style.left = 0;
      this._inner.style.top = 0;
      this._inner.style['transform-origin'] = 'left top';
    },
  
  
    _animateZoom: function (e) {
  
      var scale = this._map.getZoomScale(e.zoom),
          offset = this._map._latLngBoundsToNewLayerBounds(this._bounds, e.zoom, e.center).min;
  
      L.DomUtil.setTransform(this._dom, offset, scale);
  
      // _animateZoom() est lancÃ©e en dÃ©but de zoom
      // on aura besoin du coef de scale Ã  la fin...
      this._rescale = scale;
    },
  
  
    // la suite est une copie Ã  peine modifiÃ©e de ImageOverlay  
    bringToFront: function () {
      if (this._map) {
        L.DomUtil.toFront(this._dom);
      }
      return this;
    },
    bringToBack: function () {
      if (this._map) {
        L.DomUtil.toBack(this._dom);
      }
      return this;
    },
    getElement: function () {
      return this._dom;
    },
  
    _reset: function () {
      var dom = this._dom,
          bounds = new L.Bounds(
              this._map.latLngToLayerPoint(this._bounds.getNorthWest()),
              this._map.latLngToLayerPoint(this._bounds.getSouthEast())),
          size = bounds.getSize();
  
      L.DomUtil.setPosition(dom, bounds.min);
  
      dom.style.width  = size.x + 'px';
      dom.style.height = size.y + 'px';
    },
    _updateZIndex: function () {
      if (this._dom && this.options.zIndex !== undefined && this.options.zIndex !== null) {
        this._dom.style.zIndex = this.options.zIndex;
      }
    },
    _overlayOnError: function () {
      this.fire('error');
    },
  
    // copie extacte de ImageOverlay
    setBounds: function (bounds) {
      this._bounds = L.latLngBounds(bounds);
  
      if (this._map) {
        this._reset();
      }
      return this;
    },
    getEvents: function () {
      var events = {
        zoom: this._reset,
        viewreset: this._reset
      };
  
      if (this._zoomAnimated) {
        events.zoomanim = this._animateZoom;
      }
  
      return events;
    },
    setZIndex: function (value) {
      this.options.zIndex = value;
      this._updateZIndex();
      return this;
    },
    getBounds: function () {
      return this._bounds;
    }
  
  });
  
  //  shorthand method
  L.htmlOverlay = function(code, bounds, options) {
      return new L.HtmlOverlay(code, bounds, options);
  }
  
  
  
  // Bonus : jQuery mini-library !
  
  // only usable if you linked the jQuery library in your HTML document...
  if(typeof $ != 'undefined'){
  
    $.fn.htmlOverlay = function(coords, options){
      if(typeof options == 'undefined'){ options = {}; }
  
      var layers = [];
  
      $(this).each(function(i){ 
        // console.log("i", i);
  
        var code = $(this)[0].outerHTML;  
  
        // zoom d'origine via code html : data-zoom="15"
        if($(this).data('zoom')){
          options.zoom = $(this).data('zoom');
        }
        // position via code html : data-pos="1.54, 48.25"
        if($(this).data('pos')){
          coords = $(this).data('pos').replace(' ', '').split(',');
        }
        // console.log("coords", coords);
        // console.log("code", code);
  
        // on retire le bloc html d'origine
        $(this).remove();
  
        // on retourne le nouveau layer Leaflet
        layers.push( L.htmlOverlay(code, coords, options) );
  
      });
  
      if(layers.length>1){
        // on retourne un groupe de markers
        return L.layerGroup(layers);
  
      } else if(layers.length==1){
        // on retourne juste le layer
        return layers[0];
  
      } else {
        // aucun layer Ã  renvoyer !
        console.log("No html element to inject in map !");
        return {};
      }
    };
  
  }