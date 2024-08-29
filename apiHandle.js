import axios from "axios";
import fs from "fs";

const url_local = "http://localhost:3022"
const Auth_Token = "eyJhbGciOiJIUzI1NiJ9.anlvdGFwcGFkbWluZm9ydG9rZW4.uQD3Vd2YLr1SB55AlsB4cAAQDELIsvS_FPyUfJKEeIo"
const headers = {
    "auth-token": Auth_Token
}


function UploadData(filename,url) {
    try {
        // let data;
        fs.readFile(filename, (err, data) => {
            // console.log(JSON.parse(data));
            let datas = JSON.parse(data);
            SendData(datas, url);
        });
    } catch (error) {
        console.log(error)
    }
}


async function SendData(data, url) {
    try {

        for (let i in data) {
            await new Promise(resolve => setTimeout(resolve, 1000));

            console.log("Uploading Data ", i);

            if (i >= 0) { 
                const res = await axios({
                    url: url,
                    method: "POST",
                    headers: headers,
                    data: data[i]
                });

                // console.log(res.data.message,data[i].category_name);
                console.log(res.data.data);
            }

        }


    } catch (error) {
        console.log(error.response.data)
    }
}


const url = `${url_local}/post/add`
UploadData("filename",url);