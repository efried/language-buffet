(ns main.jsonstrings)
(enable-console-print!)
(defonce ^:string good "{\"name\": \"Nooby McNoobington\", \"winPercent\": null}")
(defonce ^:string glad "{\"name\": \"Mikhail Tal\", \"winPercent\": 85.2}")
(defonce ^:string bad "{\"name\": \"Nooby McNoobington\", 'winPercent': null}")