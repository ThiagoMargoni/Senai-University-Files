import type { PartsResponse } from "@/models/part"
import { getAxios } from "./services.config"

export const getParts = (): Promise<PartsResponse>=> {
    return getAxios().get("/parts");
}