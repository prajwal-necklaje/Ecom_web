(function(apiKey){
    (function(p,e,n,d,o){var v,w,x,y,z;o=p[d]=p[d]||{};o._q=o._q||[];
    v=['initialize','identify','updateOptions','pageLoad','track'];for(w=0,x=v.length;w<x;++w)(function(m){
        o[m]=o[m]||function(){o._q[m===v[0]?'unshift':'push']([m].concat([].slice.call(arguments,0)));};})(v[w]);
        y=e.createElement(n);y.async=!0;y.src='https://cdn.pendo.io/agent/static/'+apiKey+'/pendo.js';
        z=e.getElementsByTagName(n)[0];z.parentNode.insertBefore(y,z);})(window,document,'script','pendo');

        // This function creates visitors and accounts in Pendo
        // You will need to replace <visitor-id-goes-here> and <account-id-goes-here> with values you use in your app
        // Please use Strings, Numbers, or Bools for value types.
        pendo.initialize({
            visitor: {
                id: pendoVisitorId,
                Email :Email
            },

            account: {
                id: AccountID             
            }
        });
})('043f5c9d-f8b2-4d0f-7fd8-6020c3074f67');